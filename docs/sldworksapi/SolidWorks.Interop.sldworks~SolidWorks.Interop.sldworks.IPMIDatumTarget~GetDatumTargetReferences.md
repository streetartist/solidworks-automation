# GetDatumTargetReferences Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~GetDatumTargetReferences`

Gets the datum references for this PMI datum target.
Gets the datum references for this PMI datum target.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDatumTargetReferences() As System.Object
```

```

Dim instance As IPMIDatumTarget
Dim value As System.Object
 
value = instance.GetDatumTargetReferences()
```

```

System.object GetDatumTargetReferences()
```

```

System.Object^ GetDatumTargetReferences(); 
```

#### Return Value

Array of datum string references (see **Remarks**)

Remarks

The datum references appear in the lower half of the datum target symbols.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIDatumTarget Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget.md)  
[IPMIDatumTarget Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget_members.md)
