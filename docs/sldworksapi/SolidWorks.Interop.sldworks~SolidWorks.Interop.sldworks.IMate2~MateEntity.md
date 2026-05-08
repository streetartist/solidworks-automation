# MateEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MateEntity`

Gets an entity associated with a mate.
Gets an entity associated with a mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MateEntity( _
   ByVal Index As System.Integer _
) As MateEntity2
```

```

Dim instance As IMate2
Dim Index As System.Integer
Dim value As MateEntity2
 
value = instance.MateEntity(Index)
```

```

MateEntity2 MateEntity( 
   System.int Index
)
```

```

MateEntity2^ MateEntity( 
   System.int Index
) 
```

#### Parameters

*Index*
:   0-based index of the entity associated with the mate

#### Return Value

[Mate entity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2.md)

Remarks

To get the number of entities for this mate, call [IMate2::GetMateEntityCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetMateEntityCount.md).

Example

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)  
[Get Mates and Mate Entities (C#)](Get_Mates_and_Mate_Entities_Example_CSharp.htm)  
[Get Mates and Mate Entities (VB.NET)](Get_Mates_and_Mate_Entities_Example_VBNET.htm)  
[Get Mates and Mate Entities (VBA)](Get_Mates_and_Mate_Entities_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)
