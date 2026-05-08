# MateEntity Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace~MateEntity`

Gets the name of the mated entity associated with the specified index for this Inplace mate.
Gets the name of the mated entity associated with the specified index for this Inplace mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property MateEntity( _
   ByVal NIndex As System.Integer _
) As System.Object
```

```

Dim instance As IMateInPlace
Dim NIndex As System.Integer
Dim value As System.Object
 
value = instance.MateEntity(NIndex)
```

```

System.object MateEntity( 
   System.int NIndex
) {get;}
```

```

property System.Object^ MateEntity {
   System.Object^ get(System.int NIndex);
}
```

#### Parameters

*NIndex*
:   0-based index associated with this entity

#### Property Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [reference plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)

Remarks

To get the type of entity returned by this method, call [IMateInPlace::MateEntityType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace~MateEntityType.md) .

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateInPlace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace.md)  
[IMateInPlace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace_members.md)
