# CanBeFlipped Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~CanBeFlipped`

Gets whether this distance or angle mate can be flipped.
Gets whether this distance or angle mate can be flipped.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CanBeFlipped As System.Boolean
```

```

Dim instance As IMate2
Dim value As System.Boolean
 
value = instance.CanBeFlipped
```

```

System.bool CanBeFlipped {get;}
```

```

property System.bool CanBeFlipped {
   System.bool get();
}
```

#### Property Value

True if mate can be flipped, false if not

Remarks

Use [IMate2::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Type.md) to determine the type of mate.

Example

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)  
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)  
[Get Mates and Mate Entities (C#)](Get_Mates_and_Mate_Entities_Example_CSharp.htm)  
[Get Mates and Mate Entities (VB.NET)](Get_Mates_and_Mate_Entities_Example_VBNET.htm)  
[Get Mates and Mate Entities (VBA)](Get_Mates_and_Mate_Entities_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::Flipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Flipped.md)
