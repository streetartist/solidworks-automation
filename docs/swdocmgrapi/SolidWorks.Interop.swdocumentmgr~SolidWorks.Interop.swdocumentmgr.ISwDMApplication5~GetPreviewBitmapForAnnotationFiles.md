# GetPreviewBitmapForAnnotationFiles Method (ISwDMApplication5)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5~GetPreviewBitmapForAnnotationFiles`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5~GetPreviewBitmapForAnnotationFiles.html) on this topic. |
| GetPreviewBitmapForAnnotationFiles Method (ISwDMApplication5) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMApplication5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5.md) : GetPreviewBitmapForAnnotationFiles Method (ISwDMApplication5) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*fileName*
:   Name of annotation file

*result*
:   Error code as defined by [SwDmAnnotationFileOpenError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmAnnotationFileOpenError.md)

Gets the preview bitmap for the specified annotation file.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetPreviewBitmapForAnnotationFiles( _    ByVal fileName As System.String, _    ByRef result As SwDmAnnotationFileOpenError _ ) As System.Object ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMApplication5 Dim fileName As System.String Dim result As SwDmAnnotationFileOpenError Dim value As System.Object   value = instance.GetPreviewBitmapForAnnotationFiles(fileName, result) ``` | |

| C# |  |
| --- | --- |
| ``` System.object GetPreviewBitmapForAnnotationFiles(     System.string fileName,    out SwDmAnnotationFileOpenError result ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.Object^ GetPreviewBitmapForAnnotationFiles(  &   System.String^ fileName, &   [Out] SwDmAnnotationFileOpenError result ) ``` | |

#### Parameters

*fileName*
:   Name of annotation file

*result*
:   Error code as defined by [SwDmAnnotationFileOpenError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmAnnotationFileOpenError.md)

#### Return Value

Pointer to the preview bitmap (.bmp) (an IPictureDisp\*)

# Visual Basic for Applications (VBA) Syntax

See [SwDMApplication5::GetPreviewBitmapForAnnotationFiles](swdocumentmgr~SwDMApplication5~GetPreviewBitmapForAnnotationFiles.md).

# Example

Tailor the examples for [ISwDMDocument10::GetPreviewBitmap](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewBitmap.md) to call this method after opening an annotation file.

# Remarks

This method is only valid for getting the preview bitmaps of the following annotation file types:

\*.SLDNOTESTL

\*.SLDGTOLSTL

\*.SLDSFSTL

\*.SLDWELDSTL

\*.SLDSFFVT

\*.SLDGTOLFVT

\*.SLDWELDFVT

\*.SLDNOTEFVT

# See Also

#### 

[ISwDMApplication5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5.md)
  
[ISwDMApplication5 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5_members.md)
  
[ISwDMDocument10::GetPreviewBitmap Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewBitmap.md)
  
[ISwDMDocument10::GetPreviewPNGBitmap Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewPNGBitmap.md)
  
[ISwDMConfiguration::GetPreviewBitmap Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetPreviewBitmap.md)
  
[ISwDMConfiguration7::GetPreviewPNGBitmap Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~GetPreviewPNGBitmap.md)
  
[ISwDMSheet2::GetPreviewPNGBitmap Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmap.md)
  
[ISwDMSheet2::GetPreviewPNGBitmapBytes Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmapBytes.md)

# Availability

SOLIDWORKS Document Manager API 2024 SP1
