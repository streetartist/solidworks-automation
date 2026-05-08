# Next Method (IEnumCoEdges)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges~Next`

Gets the next coedge in the coedges enumeration.
Gets the next coedge in the coedges enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As CoEdge, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumCoEdges
Dim Celt As System.Integer
Dim Rgelt As CoEdge
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out CoEdge Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] CoEdge^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*
:   Number of coedges for the coedges enumeration

*Rgelt*
:   Pointer to an array of [coedges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md) of size Celt

*PceltFetched*
:   Number of coedges returned from the list; this value can be less than Celt if you asked for more coedges than exist, or it can be NULL if no more coedges exist

Remarks

For use in in-process DLLs only.

Example

[Enumerate Bodies (C++)](Enumerate_Bodies_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumCoEdges Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges.md)  
[IEnumCoEdges Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges_members.md)  
[ICoEdge::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetNext.md)  
[ICoEdge::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetNext.md)  
[ILoop2::GetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetFirstCoEdge.md)  
[ILoop2::IGetFirstCoEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetFirstCoEdge.md)
