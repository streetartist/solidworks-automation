# IGetMaterialPropertyValuesForFace Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetMaterialPropertyValuesForFace`

Gets the color of the specified face.
Gets the color of the specified face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMaterialPropertyValuesForFace( _
   ByVal FaceIn As System.Object _
) As System.Double
```

```

Dim instance As IComponent2
Dim FaceIn As System.Object
Dim value As System.Double
 
value = instance.IGetMaterialPropertyValuesForFace(FaceIn)
```

```

System.double IGetMaterialPropertyValuesForFace( 
   System.object FaceIn
)
```

```

System.double IGetMaterialPropertyValuesForFace( 
   System.Object^ FaceIn
) 
```

#### Parameters

*FaceIn*
:   Pointer to the face from which to get its color

#### Return Value

Color of the face

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
