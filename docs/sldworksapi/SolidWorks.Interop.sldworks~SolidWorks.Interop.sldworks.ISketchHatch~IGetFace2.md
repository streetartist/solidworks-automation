# IGetFace2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~IGetFace2`

Gets the face associated with this sketch hatch.
Gets the face associated with this sketch hatch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFace2() As Face2
```

```

Dim instance As ISketchHatch
Dim value As Face2
 
value = instance.IGetFace2()
```

```

Face2 IGetFace2()
```

```

Face2^ IGetFace2(); 
```

#### Return Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) associated with the sketch hatch or null if the operation fails

Remarks

You should not select the returned face. Only use the returned face for getting the geometry of the sketch hatch: loops, edges, equations for the edges, and so on. Do not hold onto the pointer the face after it is used as the face is transient.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md)  
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.md)  
[ISketchHatch::GetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~GetFace.md)
