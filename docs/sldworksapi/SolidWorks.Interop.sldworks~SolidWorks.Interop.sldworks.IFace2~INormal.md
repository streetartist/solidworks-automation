# INormal Property (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~INormal`

Gets the unit normal vector for any planar face.
Gets the unit normal vector for any planar face.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property INormal As System.Double
```

```

Dim instance As IFace2
Dim value As System.Double
 
instance.INormal = value
 
value = instance.INormal
```

```

System.double INormal {get; set;}
```

```

property System.double INormal {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Pointer to an array of 3 doubles (i,j,k)

Remarks

This property is read-only.

If the face is not a planar face, then this property returns 0,0,0.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::Normal Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Normal.md)
