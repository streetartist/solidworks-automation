# SaveBMP Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SaveBMP`

Saves the current view as a bitmap (BMP) file.
Saves the current view as a bitmap (BMP) file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveBMP( _
   ByVal FileNameIn As System.String, _
   ByVal WidthIn As System.Integer, _
   ByVal HeightIn As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim FileNameIn As System.String
Dim WidthIn As System.Integer
Dim HeightIn As System.Integer
Dim value As System.Boolean
 
value = instance.SaveBMP(FileNameIn, WidthIn, HeightIn)
```

```

System.bool SaveBMP( 
   System.string FileNameIn,
   System.int WidthIn,
   System.int HeightIn
)
```

```

System.bool SaveBMP( 
   System.String^ FileNameIn,
   System.int WidthIn,
   System.int HeightIn
) 
```

#### Parameters

*FileNameIn*
:   Path and file name of the new BMP file

*WidthIn*
:   Width of the BMP

*HeightIn*
:   Height of the BMP

#### Return Value

True if file is created successfully, false if not

Remarks

Include the full path to the file in FilenameIn and use filename extension of .bmp.

If WidthIn or the HeightIn is less than or equal to 0, then the view size is based on the current window size.

Example

[Save Model as Bitmap (C#)](Save_Model_as_Bitmap_Example_CSharp.htm)  
[Save Model as Bitmap (VB.NET)](Save_Model_as_Bitmap_Example_VBNET.htm)  
[Save Model as Bitmap (VBA)](Save_Model_as_Bitmap_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[ISldWorks::GetPreviewBitmapFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetPreviewBitmapFile.md)  
[ISldWorks::GetPreviewBitmap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetPreviewBitmap.md)
