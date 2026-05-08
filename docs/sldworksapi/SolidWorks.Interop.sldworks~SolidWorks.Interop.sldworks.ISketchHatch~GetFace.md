# GetFace Method (ISketchHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~GetFace`

Gets the face associated with this sketch hatch.
Gets the face associated with this sketch hatch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFace() As System.Object
```

```

Dim instance As ISketchHatch
Dim value As System.Object
 
value = instance.GetFace()
```

```

System.object GetFace()
```

```

System.Object^ GetFace(); 
```

#### Return Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) associated with the sketch hatch or null if the operation fails

Remarks

This method returns the face in the space of the sketch or drawing view. You should not select the returned face. Only use the returned face for getting the geometry of the sketch hatch: loops, edges, equations for the edges, and so on. Do not hold on to the pointer to the face after it is used as the face is transient.

Example

See the [ISketchHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md)  
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.md)  
[ISketchHatch::IGetFace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~IGetFace2.md)
