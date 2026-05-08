# Normal Property (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Normal`

Gets the unit normal vector for any planar face.
Gets the unit normal vector for any planar face.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Normal As System.Object
```

```

Dim instance As IFace2
Dim value As System.Object
 
instance.Normal = value
 
value = instance.Normal
```

```

System.object Normal {get; set;}
```

```

property System.Object^ Normal {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of 3 doubles (i,j,k)

Remarks

If the face is not a planar face, then this property returns 0,0,0.

Example

[Get Normal of Planar Face (VBA)](Get_Normal_of_Planar_Face_Example_VB.htm)  
[Get Normal of Planar Surface (VBA)](Get_Normal_of_Planar_Surface_Example_VB.htm)  
[Get Plane or Face for Sketch (VBA)](Get_Plane_or_Face_for_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::INormal Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~INormal.md)
