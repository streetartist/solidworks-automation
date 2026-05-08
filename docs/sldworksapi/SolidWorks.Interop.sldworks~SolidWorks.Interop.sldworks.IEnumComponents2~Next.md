# Next Method (IEnumComponents2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2~Next`

Gets the next component in the components enumeration.
Gets the next component in the components enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As Component2, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumComponents2
Dim Celt As System.Integer
Dim Rgelt As Component2
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out Component2 Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] Component2^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*
:   Number of components for the components enumeration

*Rgelt*
:   Pointer to an array [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) of size Celt

*PceltFetched*
:   Pointer to the number of components returned from the list.; this value can be less than Celt if you ask for more components than exist, or it can be NULL if no more components exist

Remarks

For use in in-process DLLs only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumComponents2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2.md)  
[IEnumComponents2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2_members.md)
