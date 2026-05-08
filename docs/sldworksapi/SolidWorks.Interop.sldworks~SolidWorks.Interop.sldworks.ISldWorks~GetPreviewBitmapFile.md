# GetPreviewBitmapFile Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetPreviewBitmapFile`

Gets the specified preview bitmap of a document and saves it as a Windows bitmap file (.bmp) using the specified filename.
Gets the specified preview bitmap of a document and saves it as a Windows bitmap file (.bmp) using the specified filename.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPreviewBitmapFile( _
   ByVal DocumentPath As System.String, _
   ByVal ConfigName As System.String, _
   ByVal BitMapFile As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim DocumentPath As System.String
Dim ConfigName As System.String
Dim BitMapFile As System.String
Dim value As System.Boolean
 
value = instance.GetPreviewBitmapFile(DocumentPath, ConfigName, BitMapFile)
```

```

System.bool GetPreviewBitmapFile( 
   System.string DocumentPath,
   System.string ConfigName,
   System.string BitMapFile
)
```

```

System.bool GetPreviewBitmapFile( 
   System.String^ DocumentPath,
   System.String^ ConfigName,
   System.String^ BitMapFile
) 
```

#### Parameters

*DocumentPath*
:   Path and file name of the SOLIDWORKS document whose preview bitmap (.bmp) you want to save

*ConfigName*
:   Name of the configuration

*BitMapFile*
:   Filename for the preview

#### Return Value

True if the preview bitmap (.bmp) is saved, false if not

Example

[Save Configuration Data (C#)](Save_Configuration_Data_Example_CSharp.htm)  
[Save Configuration Data (VB.NET)](Save_Configuration_Data_Example_VBNET.htm)  
[Save Configuration Data (VBA)](Save_Configuration_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetPreviewBitmap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetPreviewBitmap.md)  
[ISldWorks::PreviewDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreviewDoc.md)  
[ISldWorks::PreviewDocx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreviewDocx64.md)  
[IModelDoc2::SaveBMP Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SaveBMP.md)
