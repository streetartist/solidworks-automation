# GetPartNumberStreamFile Method (ISwDMDocument15)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetPartNumberStreamFile`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetPartNumberStreamFile.html) on this topic. |
| GetPartNumberStreamFile Method (ISwDMDocument15) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument15 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15.md) : GetPartNumberStreamFile Method (ISwDMDocument15) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*xmlFileName*
:   Name of XML file

Gets the name of the XML file generated when uploading a model to [3D Content Central](http://www.3dcontentcentral.com). The XML file is only generated if the model has a design table with a part number column.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetPartNumberStreamFile( _    ByVal xmlFileName As System.String _ ) As SwDmXmlDataError ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument15 Dim xmlFileName As System.String Dim value As SwDmXmlDataError   value = instance.GetPartNumberStreamFile(xmlFileName) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmXmlDataError GetPartNumberStreamFile(     System.string xmlFileName ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmXmlDataError GetPartNumberStreamFile(  &   System.String^ xmlFileName ) ``` | |

#### Parameters

*xmlFileName*
:   Name of XML file

#### Return Value

Status as defined in [swDmXmlDataError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmXmlDataError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument15::GetPartNumberStreamFile](swdocumentmgr~SwDMDocument15~GetPartNumberStreamFile.md).

# Remarks

Use the SOLIDWORKS Configuration Publisher to upload a model that has a design table with a part number column and other control values. (To open the Configuration Publisher in SOLIDWORKS, open a model document, right-click the top-level configuration name in the ConfigurationManager, and select **Configuration Publisher**.)

# See Also

#### 

[ISwDMDocument15 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15.md)
  
[ISwDMDocument15 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15_members.md)
  
[ISwDMDocumentManager14::Get3DCCGenericStreamFile Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14~Get3DCCGenericStreamFile.md)
  
[ISwDMDocumentManager14::Get3DCCStreamFile Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14~Get3DCCStreamFile.md)

# Availability

SOLIDWORKS Document Manager API 2011 SP0
