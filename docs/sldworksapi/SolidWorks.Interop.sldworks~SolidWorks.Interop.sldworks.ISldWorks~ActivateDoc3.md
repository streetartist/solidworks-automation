# ActivateDoc3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateDoc3`

Activates a loaded document and rebuilds it as specified.
Activates a loaded document and rebuilds it as specified.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ActivateDoc3( _
   ByVal Name As System.String, _
   ByVal UseUserPreferences As System.Boolean, _
   ByVal Option As System.Integer, _
   ByRef Errors As System.Integer _
) As System.Object
```

```

Dim instance As ISldWorks
Dim Name As System.String
Dim UseUserPreferences As System.Boolean
Dim Option As System.Integer
Dim Errors As System.Integer
Dim value As System.Object
 
value = instance.ActivateDoc3(Name, UseUserPreferences, Option, Errors)
```

```

System.object ActivateDoc3( 
   System.string Name,
   System.bool UseUserPreferences,
   System.int Option,
   out System.int Errors
)
```

```

System.Object^ ActivateDoc3( 
   System.String^ Name,
   System.bool UseUserPreferences,
   System.int Option,
   [Out] System.int Errors
) 
```

#### Parameters

*Name*
:   Name of the loaded document to activate (see **Remarks**)

*UseUserPreferences*
:   True to rebuild as per the [swRebuildOnActivation](ms-help://SolidWorks.Interop.swconst/SolidWorks/SO_Miscellaneous.htm#rebuild) system option; false to rebuild as per Option

*Option*
:   Rebuild option as defined in [swRebuildOnActivation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRebuildOnActivation_e.html) (see **Remarks**)

*Errors*
:   Status of the activate operation as defined in [swActivateDocError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swActivateDocError_e.html); if  
    no errors or warnings are encountered, then this value is 0 (see **Remarks**)

#### Return Value

[Model document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)

Remarks

This method brings the document specified in Name to the foreground of SOLIDWORKS and returns a pointer to the document.

If you do not specify a file extension in Name, the document activated is based on its filename without the file extension. This can cause problems if you have loaded two different document types with the same name (e.g., **12345.sldprt** and **12345.sldasm)**. To avoid this problem, specify the file extension in Name or check the document type after it is activated using [IModelDoc2::GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetType.md).

If the document needs a rebuild upon activation, and you have specified Option with [swRebuildOnActivation\_e.swDontRebuildActiveDoc](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRebuildOnActivation_e.html), then the activated document is not rebuilt, and Errors contains [swActivateDocError\_e.swDocNeedsRebuildWarning](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swActivateDocError_e.html). You can then rebuild the document using [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md).

If the document needs a rebuild upon activation, and you have specified Option with [swRebuildOnActivation\_e.swUserDecision](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRebuildOnActivation_e.html), then a dialog displays asking whether to rebuild the document.

|  |  |
| --- | --- |
| **If the user answers...** | **Then the activated document is...** |
| No | Not rebuilt, and Errors contains [swActivateDocError\_e.swDocNeedsRebuildWarning](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swActivateDocError_e.html) |
| Yes | Rebuilt immediately |

Example

[Rebuild Document on Activation (VBA)](Rebuild_Document_on_Activation_Example_VB.htm)  
[Rebuild Document on Activation (VB.NET)](Rebuild_Document_on_Activation_Example_VBNET.htm)  
[Rebuild Document on Activation (C#)](Rebuild_Document_on_Activation_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::IActivateDoc3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActivateDoc3.md)  
[ISldWorks::ActiveDoc Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.md)  
[ISldWorks::IActiveDoc2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.md)  
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.md)  
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.md)  
[ISldWorks::CloseAndReopen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAndReopen.md)  
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.md)  
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.md)  
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.md)  
[ISldWorks::GetOpenFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName.md)  
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.md)  
[ISldWorks::IGetOpenDocumentByName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.md)  
[ISldWorks::LoadFile4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md)  
[ISldWorks::OpenDoc7 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md)
