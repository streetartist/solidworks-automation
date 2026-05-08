# InsertSketchPictureData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPictureData`

Inserts a picture into the current sketch.
Inserts a picture into the current sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertSketchPictureData( _
   ByVal Width As System.Short, _
   ByVal Height As System.Short, _
   ByVal PDataIn As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim Width As System.Short
Dim Height As System.Short
Dim PDataIn As System.Integer
 
instance.InsertSketchPictureData(Width, Height, PDataIn)
```

```

void InsertSketchPictureData( 
   System.short Width,
   System.short Height,
   System.int PDataIn
)
```

```

void InsertSketchPictureData( 
   System.short Width,
   System.short Height,
   System.int PDataIn
) 
```

#### Parameters

*Width*
:   Width of the image

*Height*
:   Height of the image

*PDataIn*
:   Pointer to a raw bitmap (HBITMAP) cast as a long

Remarks

If your application must be x64 compatible, then use [IModelDoc2::InsertSketchPictureDatax64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPictureDatax64.md).

A copy of the specified bitmap data is created. The SOLIDWORKS software does not release your bitmap object.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::InsertSketchPicture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPicture.md)
