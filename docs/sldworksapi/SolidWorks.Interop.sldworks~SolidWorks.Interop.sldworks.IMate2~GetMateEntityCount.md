# GetMateEntityCount Method (IMate2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetMateEntityCount`

Gets the number of entities for this mate.
Gets the number of entities for this mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMateEntityCount() As System.Integer
```

```

Dim instance As IMate2
Dim value As System.Integer
 
value = instance.GetMateEntityCount()
```

```

System.int GetMateEntityCount()
```

```

System.int GetMateEntityCount(); 
```

#### Return Value

Number of entities for this mate

Remarks

Call this method before calling [IMate2::MateEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MateEntity.md) to get the number of entities in the mate.

Example

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)  
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)
