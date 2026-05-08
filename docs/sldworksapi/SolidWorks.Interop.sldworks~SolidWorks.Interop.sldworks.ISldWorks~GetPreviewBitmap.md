# GetPreviewBitmap Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetPreviewBitmap`

Gets the preview bitmap (.bmp) for the specified configuration, regardless if the SOLIDWORKS document is open or closed.
Gets the preview bitmap (.bmp) for the specified configuration, regardless if the SOLIDWORKS document is open or closed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPreviewBitmap( _
   ByVal FilePathName As System.String, _
   ByVal ConfigName As System.String _
) As System.Object
```

```

Dim instance As ISldWorks
Dim FilePathName As System.String
Dim ConfigName As System.String
Dim value As System.Object
 
value = instance.GetPreviewBitmap(FilePathName, ConfigName)
```

```

System.object GetPreviewBitmap( 
   System.string FilePathName,
   System.string ConfigName
)
```

```

System.Object^ GetPreviewBitmap( 
   System.String^ FilePathName,
   System.String^ ConfigName
) 
```

#### Parameters

*FilePathName*
:   Path and file name of the SOLIDWORKS document

*ConfigName*
:   Name of the configuration

#### Return Value

Dispatch pointer to IPictureDisp interface, the preview bitmap (.bmp) (see Remarks)

Remarks

The preview bitmap is the bitmap (.bmp) that appears in the Preview box on the Open dialog.

NOTES:

- Currently only in-process applications (that is, macros or add-ins) can use this method; out-of-process applications (that is, executables) will get an automation error because the IPictureDisp interface cannot be marshalled across process boundaries. This is a Microsoft behavior by design. See the Microsoft Knowledge Base for details.
- This method is not supported in macros or out-of-process applications in SOLIDWORKS x64.

Example

[Get Preview Bitmap (VBA)](Get_Preview_Bitmap_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::PreviewDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreviewDoc.md)  
[ISldWorks::PreviewDocx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreviewDocx64.md)  
[ISldWorks::GetPreviewBitmapFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetPreviewBitmapFile.md)  
[IModelDoc2::SaveBMP Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SaveBMP.md)
