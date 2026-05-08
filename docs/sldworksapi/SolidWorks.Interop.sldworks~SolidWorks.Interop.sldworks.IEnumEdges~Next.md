# Next Method (IEnumEdges)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges~Next`

Gets the next edge in the edges enumeration.
Gets the next edge in the edges enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Edge, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumEdges
Dim Celt As System.Integer
Dim Rgelt As Edge
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out Edge Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] Edge^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*
:   Number edges for the edges enumeration

*Rgelt*
:   Pointer to an array of edges of size Celt

*PceltFetched*
:   Pointer to the number of edges returned from the list; this value can be less than Celt if you ask for more edges than exist, or it can be NULL if no more edges exist.

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumEdges Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges.md)  
[IEnumEdges Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges_members.md)
