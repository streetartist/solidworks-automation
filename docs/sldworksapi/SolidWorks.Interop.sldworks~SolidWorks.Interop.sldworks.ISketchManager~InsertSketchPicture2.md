# InsertSketchPicture2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchPicture2`

Inserts a picture on the current drawing sketch.
Inserts a picture on the current drawing sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSketchPicture2( _
   ByVal FileName As System.String, _
   ByVal HighestResolution As System.Boolean _
) As SketchPicture
```

```

Dim instance As ISketchManager
Dim FileName As System.String
Dim HighestResolution As System.Boolean
Dim value As SketchPicture
 
value = instance.InsertSketchPicture2(FileName, HighestResolution)
```

```

SketchPicture InsertSketchPicture2( 
   System.string FileName,
   System.bool HighestResolution
)
```

```

SketchPicture^ InsertSketchPicture2( 
   System.String^ FileName,
   System.bool HighestResolution
) 
```

#### Parameters

*FileName*
:   Path to image file including file extension

*HighestResolution*
:   True to insert images up to 8192 pixels without compression, false to compress images to 2048 pixels before insertion (see **Remarks**)

#### Return Value

[Picture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)

Remarks

If the document type is not a drawing, then HighestResolution defaults to false.

Example

[Flip Sketch Picture (VBA)](Flip_Sketch_Picture_Example_VB.htm)  
[Flip Sketch Picture (VB.NET)](Flip_Sketch_Picture_Example_VBNET.htm)  
[Flip Sketch Picture (C#)](Flip_Sketch_Picture_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
