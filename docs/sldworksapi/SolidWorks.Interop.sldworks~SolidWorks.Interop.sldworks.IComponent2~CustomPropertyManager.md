# CustomPropertyManager Property (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~CustomPropertyManager`

Gets the configuration-specific custom property manager for this assembly component.
Gets the configuration-specific custom property manager for this assembly component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CustomPropertyManager( _
   ByVal ConfigurationName As System.String _
) As System.Object
```

```

Dim instance As IComponent2
Dim ConfigurationName As System.String
Dim value As System.Object
 
value = instance.CustomPropertyManager(ConfigurationName)
```

```

System.object CustomPropertyManager( 
   System.string ConfigurationName
) {get;}
```

```

property System.Object^ CustomPropertyManager {
   System.Object^ get(System.String^ ConfigurationName);
}
```

#### Parameters

*ConfigurationName*
:   Name of the configuration for which to get custom properties; empty string to obtain document-specific custom properties

#### Property Value

[ICustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)

Example

'VBA

'=======================================

'Preconditions:

' 1. Open *public\_documents***\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\mbd\mbdadvanced\beater\_assembly.sldasm**.

' 2. Create a configuration-specific custom property for **pan cross head<3>.**

'     a. Open **pan cross head<3>.**

'     b. Select the ConfigurationManager tab.

'     c. Right-click on CR-PHMS 0.073-72x0.125x0.125-N and select **Properties**.

'     d. In Configuration Properties, click **Custom Properties...**

'     e. On the Configuration Specific tab, create a custom property of type Text and provide a value.

' 2. Open the Immediate window.

'Postconditions: Displays the configuration-specific custom properties of all of the components in the assembly.

'========================================

Option Explicit  
Dim swApp As SldWorks.SldWorks  
Dim swModelDoc As SldWorks.ModelDoc2  
Dim swCompCur As SldWorks.Component2  
Dim sCompName As String  
Dim sRefConfigName As String  
Dim swCompModelDoc As SldWorks.ModelDoc2  
Dim swCompModelDocExt As SldWorks.ModelDocExtension  
Dim swCompModelDocConf As SldWorks.Configuration  
Dim swCompModelDocCustPropMgr As SldWorks.CustomPropertyManager  
Dim swAssyDoc As SldWorks.AssemblyDoc  
Dim vComps As Variant  
Dim vComfigNames As Variant  
Dim iCompIndex As Integer  
Dim swCustPropMgrOfCurComp As SldWorks.CustomPropertyManager  
Dim sConfigName As String  
Dim iConfigIndex As Integer  
Dim boolstatus As Boolean  
Dim longstatus As Long, longwarnings As Long

Sub main()

    Set swApp = Application.SldWorks  
    Set swModelDoc = swApp.ActiveDoc  
     
    If swModelDoc.GetType = swDocASSEMBLY Then  
     
        Set swAssyDoc = swModelDoc  
        
        vComps = swAssyDoc.GetComponents(True)  
        If Not IsEmpty(vComps) Then  
    
            For iCompIndex = 0 To UBound(vComps)  
                Set swCompCur = vComps(iCompIndex)  
                sCompName = swCompCur.Name2  
                Debug.Print ""  
                Debug.Print "\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*"  
                Debug.Print "Component: " & sCompName  
                 
                sRefConfigName = swCompCur.ReferencedConfiguration  
                Debug.Print "Referenced configuration: " & sRefConfigName  
               
                'Get the component's document-level CustomPropertyManager  
                Set swCustPropMgrOfCurComp = swCompCur.**CustomPropertyManager**("")  
                DisplayCustomPropInfo "", swCustPropMgrOfCurComp  
                 
                Set swCompModelDoc = swCompCur.GetModelDoc2  
                vComfigNames = swCompModelDoc.GetConfigurationNames  
                                
                'Get the configuration-specific CustomPropertyManager for each of the current component's configurations  
                If Not IsEmpty(vComfigNames) Then  
                    For iConfigIndex = 0 To UBound(vComfigNames)  
                        sConfigName = vComfigNames(iConfigIndex)  
                        Set swCustPropMgrOfCurComp = swCompCur.**CustomPropertyManager**(sConfigName)  
                        DisplayCustomPropInfo sConfigName, swCustPropMgrOfCurComp  
                    Next iConfigIndex  
                End If

            Next iCompIndex  
             
            Debug.Print ""  
        End If  
    End If  
End Sub

Sub DisplayCustomPropInfo(sConfigName As String, swCustPropMgr As CustomPropertyManager)  
    Dim CustPropCount As Long  
    Dim sValOut As String  
    Dim sResValOut As String  
    Dim bWasResolved As Boolean  
    Dim bLinkToProperty As Boolean  
    Dim lResult As Long  
    Dim vNames As Variant  
    Dim i As Long  
    Dim lValue As Long  
    Dim bValue As Boolean  
    Dim lLinkPropValue As Long  
    Dim lSetValue As Long  
    Dim PropNames As Variant  
    Dim PropTypes As Variant  
    Dim PropValues As Variant  
    Dim Resolved As Variant  
    Dim PropLink As Variant  
    Dim lGetAllValue As Long  
    Dim lPropIndex As Long

    Debug.Print ""  
    If sConfigName = "" Then  
        Debug.Print "Custom properties: Document level"  
    Else  
        Debug.Print "Custom properties: Configuration = " & sConfigName  
    End If  
     
    If swCustPropMgr Is Nothing Then  
        Debug.Print "   \*\*\*\*\* CustomPropertyManager() Failed! \*\*\*\*\*"  
    Else  
     
         
        CustPropCount = swCustPropMgr.**Count**  
        Debug.Print "   Count: " & CustPropCount  
         
        If CustPropCount > 0 Then  
             
            vNames = swCustPropMgr.**GetNames**  
      
            For i = 0 To UBound(vNames)  
                Debug.Print "   " & vNames(i)

                lResult = swCustPropMgr.**Get6**(vNames(i), False, sValOut, sResValOut, bWasResolved, bLinkToProperty)

                Debug.Print "      Value: " & sResValOut & "      Evaluated value: " & sValOut  
                 
                lValue = swCustPropMgr.**GetType2**(vNames(i))  
                Select Case lValue  
                    Case swCustomInfoUnknown  
                        Debug.Print "      Type: swCustomInfoUnknown"  
                    Case swCustomInfoNumber  
                        Debug.Print "      Type: swCustomInfoNumber"  
                    Case swCustomInfoDouble  
                        Debug.Print "      Type: swCustomInfoDouble"  
                    Case swCustomInfoYesOrNo  
                        Debug.Print "      Type: swCustomInfoYesOrNo"  
                    Case swCustomInfoText  
                        Debug.Print "      Type: swCustomInfoText"  
                    Case swCustomInfoDate  
                        Debug.Print "      Type: swCustomInfoDate"  
                    Case Else  
                        Debug.Print "      Type: Value not in enum!"  
                End Select  
                 
             
                bValue = swCustPropMgr.IsCustomPropertyEditable(vNames(i), sConfigName)  
                Debug.Print "      Editable: " & bValue  
                 
      
                lLinkPropValue = swCustPropMgr.**LinkProperty**(vNames(i), True)  
                Select Case lLinkPropValue  
                    Case swCustomLinkSetResult\_OK  
                        Debug.Print "      LinkProperty(True): swCustomLinkSetResult\_OK"  
                    Case swCustomLinkSetResult\_NotPresent  
                        Debug.Print "      LinkProperty(True): swCustomLinkSetResult\_NotPresent"  
                    Case swCustomLinkSetResult\_Legacy  
                        Debug.Print "      LinkProperty(True): swCustomLinkSetResult\_Legacy"  
                    Case swCustomLinkSetResult\_UserProp  
                        Debug.Print "      LinkProperty(True): swCustomLinkSetResult\_UserProp"  
                    Case Else  
                        Debug.Print "      Type: Value not in enum!"  
                End Select  
                         
                lLinkPropValue = swCustPropMgr.**LinkProperty**(vNames(i), False)  
                Select Case lLinkPropValue  
                    Case swCustomLinkSetResult\_OK  
                        Debug.Print "      LinkProperty(False): swCustomLinkSetResult\_OK"  
                    Case swCustomLinkSetResult\_NotPresent  
                        Debug.Print "      LinkProperty(False): swCustomLinkSetResult\_NotPresent"  
                    Case swCustomLinkSetResult\_Legacy  
                        Debug.Print "      LinkProperty(False): swCustomLinkSetResult\_Legacy"  
                    Case swCustomLinkSetResult\_UserProp  
                        Debug.Print "      LinkProperty(False): swCustomLinkSetResult\_UserProp"  
                    Case Else  
                        Debug.Print "      Type: Value not in enum!"  
                End Select  
                 
            Next i  
             
            lGetAllValue = swCustPropMgr.**GetAll3**(PropNames, PropTypes, PropValues, Resolved, PropLink)  
            For lPropIndex = 0 To UBound(PropNames)  
                Debug.Print "      " & PropNames(lPropIndex) & ", " & PropTypes(lPropIndex) & ", " & PropValues(lPropIndex) & ", " & Resolved(lPropIndex) & ", " & PropLink(lPropIndex)  
            Next lPropIndex  
             
        End If  
    End If  
End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
