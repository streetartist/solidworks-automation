# Get3DCCStreamFile Method (ISwDMDocument14)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14~Get3DCCStreamFile`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14~Get3DCCStreamFile.html) on this topic. |
| Get3DCCStreamFile Method (ISwDMDocument14) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument14 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14.md) : Get3DCCStreamFile Method (ISwDMDocument14) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*xmlFileName*
:   Name of file to which to save the configuration rules data

Exports an XML file with the 3D Content Central (3DCC) original format configuration rules built into this document by the SOLIDWORKS Configuration Publisher.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function Get3DCCStreamFile( _    ByVal xmlFileName As System.String _ ) As SwDmXmlDataError ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument14 Dim xmlFileName As System.String Dim value As SwDmXmlDataError   value = instance.Get3DCCStreamFile(xmlFileName) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmXmlDataError Get3DCCStreamFile(     System.string xmlFileName ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmXmlDataError Get3DCCStreamFile(  &   System.String^ xmlFileName ) ``` | |

#### Parameters

*xmlFileName*
:   Name of file to which to save the configuration rules data

#### Return Value

Status as defined in [swDmXmlDataError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmXmlDataError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument14::Get3DCCStreamFile](swdocumentmgr~SwDMDocument14~Get3DCCStreamFile.md).

# Example

[Get 3D Content Central Stream Files (VB.NET)](Get_3D_Content_Central_Stream_Files_Example_VBNET.htm)
  
[Get 3D Content Central Stream Files (C#)](Get_3D_Content_Central_Stream_Files_Example_CSharp.htm)

# Remarks

Designers use the SOLIDWORKS Configuration Publisher to build configuration rules into their documents to constrain how the documents are seen by users who download them from [3D Content Central](http://www.3dcontentcentral.com). (To open the Configuration Publisher in SOLIDWORKS, open a document, right-click on the top-level configuration name in the ConfigurationManager, and click **Configuration Publisher**).

Configuration rules are typically functions of the document's design table parameters. These rules specify how to display the document in different configurations. The Configuration Publisher inserts into the document the configuration rules in two formats: original and [generic](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14~Get3DCCGenericStreamFile.md).

This method allows user-interface developers to extract configuration rule information in the original format. Developers can then modify the extracted XML file to display the document in a format that differs from the 3D Content Central format.

The Configuration Publisher can also upload documents along with their configuration rules to 3D Content Central. See the 3D Content Central web site to learn more.

# See Also

#### 

[ISwDMDocument14 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14.md)
  
[ISwDMDocument14 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14_members.md)
  
[ISwDMDocument15::GetPartNumberStreamFile Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetPartNumberStreamFile.md)

# Availability

SOLIDWORKS Document Manager API 2010 SP0
