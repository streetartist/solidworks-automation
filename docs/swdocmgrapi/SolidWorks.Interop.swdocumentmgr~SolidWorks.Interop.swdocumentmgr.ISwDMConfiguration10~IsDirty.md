# IsDirty Method (ISwDMConfiguration10)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10~IsDirty`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10~IsDirty.html) on this topic. |
| IsDirty Method (ISwDMConfiguration10) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10.md) : IsDirty Method (ISwDMConfiguration10) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets whether this configuration is dirty (i.e., needs to be updated).

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function IsDirty() As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration10 Dim value As System.Boolean   value = instance.IsDirty() ``` | |

| C# |  |
| --- | --- |
| ``` System.bool IsDirty() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool IsDirty(); ``` | |

#### Return Value

True if the configuration is dirty, false if not

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration10::IsDirty](swdocumentmgr~SwDMConfiguration10~IsDirty.md).

# Example

**Visual Basic for Applications (VBA)**

Option Explicit

Sub main()

    Const sLicenseKey           As String = "*your\_license\_key*" ' Specify your license key

    Const sDocFileName          As String = "c:\test\Wiper\_Plate\_Assy.SLDASM" ' Specify your document  
    
    Dim swClassFact             As SwDocumentMgr.SwDMClassFactory

    Dim swDocMgr                As SwDocumentMgr.SwDMApplication

    Dim swDoc                   As SwDocumentMgr.SwDMDocument

    Dim swCfgMgr                As SwDocumentMgr.SwDMConfigurationMgr

    Dim vCfgNameArr             As Variant

    Dim vCfgName                As Variant

    Dim swCfg                   As SwDocumentMgr.SwDMConfiguration10

    Dim nDocType                As Long

    Dim nRetVal                 As Long

    Dim i                       As Long

    Dim bRet                    As Boolean

    ' Determine type of SOLIDWORKS file based on filename extension

    If InStr(LCase(sDocFileName), "sldprt") > 0 Then

        nDocType = swDmDocumentPart

    ElseIf InStr(LCase(sDocFileName), "sldasm") > 0 Then

        nDocType = swDmDocumentAssembly

    ElseIf InStr(LCase(sDocFileName), "slddrw") > 0 Then

        nDocType = swDmDocumentDrawing

    Else

        ' Probably not a SOLIDWORKS file

        nDocType = swDmDocumentUnknown

        ' So cannot open

        Exit Sub

    End If

    Set swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")

    Set swDocMgr = swClassFact.**GetApplication**(sLicenseKey)

    Set swDoc = swDocMgr.**GetDocument**(sDocFileName, nDocType, True, nRetVal): Debug.Assert swDmDocumentOpenErrorNone = nRetVal

    Set swCfgMgr = swDoc.**ConfigurationManager**

    Debug.Print "File = " & swDoc.FullName  
    Debug.Print "  ActiveCfgName    = " & swCfgMgr.**GetActiveConfigurationName**

    vCfgNameArr = swCfgMgr.**GetConfigurationNames**

    For Each vCfgName In vCfgNameArr  
        Set swCfg = swCfgMgr.**GetConfigurationByName**(vCfgName)  
        Debug.Print vCfgName & " -> Dirty Flag = " & swCfg.**IsDirty**  
     Next

End Sub

# Remarks

This method only supports documents saved in SOLIDWORKS 2006 and later.

If the configuration is dirty, then you can update its date by activating the configuration in SOLIDWORKS and saving the document while the configuration is active.

# See Also

#### 

[ISwDMConfiguration10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10.md)
  
[ISwDMConfiguration10 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10_members.md)

# Availability

SOLIDWORKS Document Manager API 2008 SP5
