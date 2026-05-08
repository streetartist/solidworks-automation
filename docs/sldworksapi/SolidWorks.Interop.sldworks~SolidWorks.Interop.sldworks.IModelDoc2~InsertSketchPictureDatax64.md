# InsertSketchPictureDatax64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPictureDatax64`

Inserts a picture into the current sketch in 64-bit applications.
Inserts a picture into the current sketch in 64-bit applications.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertSketchPictureDatax64( _
   ByVal Width As System.Integer, _
   ByVal Height As System.Integer, _
   ByVal PDataIn As System.Long _
) 
```

```

Dim instance As IModelDoc2
Dim Width As System.Integer
Dim Height As System.Integer
Dim PDataIn As System.Long
 
instance.InsertSketchPictureDatax64(Width, Height, PDataIn)
```

```

void InsertSketchPictureDatax64( 
   System.int Width,
   System.int Height,
   System.long PDataIn
)
```

```

void InsertSketchPictureDatax64( 
   System.int Width,
   System.int Height,
   System.int64 PDataIn
) 
```

#### Parameters

*Width*
:   Width of the image

*Height*
:   Height of the image

*PDataIn*
:   Pointer to a raw bitmap (HBITMAP) cast as a LONGLONG

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

A copy of the specified bitmap data is created. The SOLIDWORKS software does not release your bitmap object.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::InsertSketchPictureData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPictureData.md)
