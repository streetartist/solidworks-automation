# Transform Property (IRefPlane)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~Transform`

Gets the plane transform with respect to the world.
Gets the plane transform with respect to the world.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Transform As MathTransform
```

```

Dim instance As IRefPlane
Dim value As MathTransform
 
value = instance.Transform
```

```

MathTransform Transform {get;}
```

```

property MathTransform^ Transform {
   MathTransform^ get();
}
```

#### Property Value

[Transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

Example

[Get the Normal and Origin of a Reference Plane Using Its Transform (VBA)](Get_the_Normal_and_Origin_of_a_Reference_Plane_Using_Its_Transform_Example_VB.htm)  
[Get Transform of Plane (VBA)](Get_Transform_of_Plane_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)  
[IRefPlane Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane_members.md)
