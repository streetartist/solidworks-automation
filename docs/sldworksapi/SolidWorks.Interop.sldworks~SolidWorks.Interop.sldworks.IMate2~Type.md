# Type Property (IMate2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Type`

Gets the type of mate.
Gets the type of mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Type As System.Integer
```

```

Dim instance As IMate2
Dim value As System.Integer
 
value = instance.Type
```

```

System.int Type {get;}
```

```

property System.int Type {
   System.int get();
}
```

#### Property Value

Type of mate as defined by [swMateType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateType_e.html)

Example

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)  
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)  
[Get Mates (C#)](Get_Mates_Example_CSharp.htm)  
[Get Mates (VB.NET)](Get_Mates_Example_VBNET.htm)  
[Get Mates (VBA)](Get_Mates_Example_VB.htm)  
[Get Mates and Mate Entities (C#)](Get_Mates_and_Mate_Entities_Example_CSharp.htm)  
[Get Mates and Mate Entities (VB.NET)](Get_Mates_and_Mate_Entities_Example_VBNET.htm)  
[Get Mates and Mate Entities (VBA)](Get_Mates_and_Mate_Entities_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::LockMagneticMate Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~LockMagneticMate.md)
