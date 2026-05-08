# ReferencedFeatures Method (ISwDMExternalReferenceOption2)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2~ReferencedFeatures`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2~ReferencedFeatures.html) on this topic. |
| ReferencedFeatures Method (ISwDMExternalReferenceOption2) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMExternalReferenceOption2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2.md) : ReferencedFeatures Method (ISwDMExternalReferenceOption2) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*FeatureNames*
:   Array of strings of the names of the referenced features

*FeatureTypes*
:   Array of strings of the types of referenced features

Gets the names and types of reference features in the document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function ReferencedFeatures( _    ByRef FeatureNames As System.Object, _    ByRef FeatureTypes As System.Object _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMExternalReferenceOption2 Dim FeatureNames As System.Object Dim FeatureTypes As System.Object Dim value As System.Boolean   value = instance.ReferencedFeatures(FeatureNames, FeatureTypes) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool ReferencedFeatures(     out System.object FeatureNames,    out System.object FeatureTypes ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool ReferencedFeatures(  &   [Out] System.Object^ FeatureNames, &   [Out] System.Object^ FeatureTypes ) ``` | |

#### Parameters

*FeatureNames*
:   Array of strings of the names of the referenced features

*FeatureTypes*
:   Array of strings of the types of referenced features

#### Return Value

True if the method successfully executes, false if the method fails to execute

# Visual Basic for Applications (VBA) Syntax

See [SwDMExternalReferenceOption2::ReferencedFeatures](swdocumentmgr~SwDMExternalReferenceOption2~ReferencedFeatures.md).

# Example

[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
  
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)

# See Also

#### 

[ISwDMExternalReferenceOption2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2.md)
  
[ISwDMExternalReferenceOption2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2_members.md)

# Availability

SOLIDWORKS Document Manager API 2014 SP0
