# Next Method (IEnumLoops)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops~Next`

Obsolete. Superseded by IEnumLoops2::Next.
Obsolete. Superseded by [IEnumLoops2::Next](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2~Next.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Loop, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumLoops
Dim Celt As System.Integer
Dim Rgelt As Loop
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out Loop Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] Loop^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*

*Rgelt*

*PceltFetched*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumLoops Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops.md)  
[IEnumLoops Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops_members.md)
