# GetSwDmSettingInteger Method (ISwDMDocument19)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~GetSwDmSettingInteger`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~GetSwDmSettingInteger.html) on this topic. |
| GetSwDmSettingInteger Method (ISwDMDocument19) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.md) : GetSwDmSettingInteger Method (ISwDMDocument19) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*DmSetting*
:   Setting as defined by [swDmDocumentUnitsIntegerValue\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDocumentUnitsIntegerValue_e.md)

Gets the specified document setting.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetSwDmSettingInteger( _    ByVal DmSetting As System.Integer _ ) As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument19 Dim DmSetting As System.Integer Dim value As System.Integer   value = instance.GetSwDmSettingInteger(DmSetting) ``` | |

| C# |  |
| --- | --- |
| ``` System.int GetSwDmSettingInteger(     System.int DmSetting ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int GetSwDmSettingInteger(  &   System.int DmSetting ) ``` | |

#### Parameters

*DmSetting*
:   Setting as defined by [swDmDocumentUnitsIntegerValue\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmDocumentUnitsIntegerValue_e.md)

#### Return Value

Value for DmSetting

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument19::GetSwDmSettingInteger](swdocumentmgr~SwDMDocument19~GetSwDmSettingInteger.md).

# Example

See the [ISwDMDocument19](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.md) examples.

# Remarks

This method works only with documents saved in SOLIDWORKS 2015 or later.

# See Also

#### 

[ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.md)
  
[ISwDMDocument19 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19_members.md)
  
[ISwDMDocument19::GetSwDmSettingToggle Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19~GetSwDmSettingToggle.md)

# Availability

SOLIDWORKS Document Manager API 2015 SP0
