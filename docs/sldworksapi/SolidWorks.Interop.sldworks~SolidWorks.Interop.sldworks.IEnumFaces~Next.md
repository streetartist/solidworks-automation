# Next Method (IEnumFaces)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces~Next`

Obsolete. Superseded by IEnumFaces2::Next.
Obsolete. Superseded by [IEnumFaces2::Next](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2~Next.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Face, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumFaces
Dim Celt As System.Integer
Dim Rgelt As Face
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out Face Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] Face^ Rgelt,
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

[IEnumFaces Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces.md)  
[IEnumFaces Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces_members.md)
