# SetComponentIdentifiers Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetComponentIdentifiers`

Allows you to specify the primary, ( secondary ), and &lt; tertiary &gt; elements to display for the components in the FeatureManager design tree.
Allows you to specify the primary, ( secondary ), and < tertiary > elements to display for the components in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetComponentIdentifiers( _
   ByVal Primary As System.Integer, _
   ByVal Secondary As System.Integer, _
   ByVal Tertiary As System.Integer _
) As System.Integer
```

```

Dim instance As IFeatureManager
Dim Primary As System.Integer
Dim Secondary As System.Integer
Dim Tertiary As System.Integer
Dim value As System.Integer
 
value = instance.SetComponentIdentifiers(Primary, Secondary, Tertiary)
```

```

System.int SetComponentIdentifiers( 
   System.int Primary,
   System.int Secondary,
   System.int Tertiary
)
```

```

System.int SetComponentIdentifiers( 
   System.int Primary,
   System.int Secondary,
   System.int Tertiary
) 
```

#### Parameters

*Primary*
:   Component identifier as defined by [swComponentIdentifier\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentIdentifier_e.html)

*Secondary*
:   Component identifier(s) as defined by swComponentIdentifier\_e

*Tertiary*
:   Component identifier(s) as defined by swComponentIdentifier\_e

#### Return Value

Result code as defined by [swSetComponentIdentifierResult\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSetComponentIdentifierResult_e.html)

Remarks

This method:

- Works in both SOLIDWORKS Desktop and [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm).
- Is analogous to right-clicking on the top-level component in the FeatureManager design tree and selecting **Tree Display > Component Name and Description**.

Example

'VBA

'-------------------------------------------------------  
' Preconditions:  
' 1. Open *public\_documents***\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\smartcomponents\pillow\_block.sldasm**.  
' 2. Widen the FeatureManager design tree.  
'  
' Postconditions: Inspect the FeatureManager design tree and press F5 after each Stop.  
'  
' Notes: Because the model is used elsewhere, do not save changes.  
'-------------------------------------------------------  
Option Explicit  
Dim swApp As SldWorks.SldWorks  
Dim Part As SldWorks.ModelDoc2  
Dim swFeatMgr As SldWorks.FeatureManager  
Dim compIdentifierRet As Long

Sub main()  
    Set swApp = Application.SldWorks  
    Set Part = swApp.ActiveDoc  
    Set swFeatMgr = Part.FeatureManager  
     
    ' Do show configuration or display state name if only one exists  
    swFeatMgr.**HideComponentSingleConfigurationOrDisplayStateNames** = False

    ' Set primary identifier  
    compIdentifierRet = swFeatMgr.**SetComponentIdentifiers**(swComponentIdentifier\_ComponentName, 0, 0)  
    Stop  
     
    compIdentifierRet = swFeatMgr.**SetComponentIdentifiers**(swComponentIdentifier\_ComponentDescription, 0, 0)  
    Stop  
     
    ' Set primary and secondary identifiers  
    compIdentifierRet = swFeatMgr.**SetComponentIdentifiers**(swComponentIdentifier\_ComponentName, swComponentIdentifier\_ConfigurationName, 0)  
    Stop  
     
    compIdentifierRet = swFeatMgr.**SetComponentIdentifiers**(swComponentIdentifier\_ComponentName, swComponentIdentifier\_ConfigurationDescription, 0)  
    Stop  
     
    compIdentifierRet = swFeatMgr.**SetComponentIdentifiers**(swComponentIdentifier\_ComponentName, swComponentIdentifier\_ComponentDescription, 0)  
    Stop  
     
    'Set primary, secondary, and tertiary identifiers  
    compIdentifierRet = swFeatMgr.**SetComponentIdentifiers**(swComponentIdentifier\_ComponentName, swComponentIdentifier\_ConfigurationName + swComponentIdentifier\_ConfigurationDescription + swComponentIdentifier\_ComponentDescription, swComponentIdentifier\_DisplayStateName)  
    Stop  
     
    
End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::ComponentPrimaryIdentifier Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ComponentPrimaryIdentifier.md)  
[IFeatureManager::ComponentSecondaryIdentifier Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ComponentSecondaryIdentifier.md)  
[IFeatureManager::ComponentTertiaryIdentifier Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ComponentTertiaryIdentifier.md)
