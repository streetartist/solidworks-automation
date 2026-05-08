# InsertSketchPicture Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPicture`

Inserts a picture into the current sketch.
Inserts a picture into the current sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSketchPicture( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.InsertSketchPicture(FileName)
```

```

System.bool InsertSketchPicture( 
   System.string FileName
)
```

```

System.bool InsertSketchPicture( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path to image file including file extension

#### Return Value

True if successful, false if not

Remarks

Supported image types are:

- Windows bitmap (\*.bmp)
- Tagged Image Format (\*.tif)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::InsertSketchPictureData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPictureData.md)
