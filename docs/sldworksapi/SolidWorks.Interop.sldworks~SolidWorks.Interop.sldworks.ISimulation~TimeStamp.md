# TimeStamp Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation~TimeStamp`

Obsolete. Not superseded.
Obsolete. Not superseded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property TimeStamp As System.Integer
```

```

Dim instance As ISimulation
Dim value As System.Integer
 
value = instance.TimeStamp
```

```

System.int TimeStamp {get;}
```

```

property System.int TimeStamp {
   System.int get();
}
```

#### Property Value

Time stamp for this Physical Simulation (see **Remarks**)

Remarks

|  |  |
| --- | --- |
| **If a...** | **Then...** |
| New Physical Simulation is calculated | The time stamp (return value) changes |
| Physical Simulation does not exist or it was deleted | 0 is returned |
| Physical Simulation was created using SOLIDWORKS 2005 or earlier | -1 is returned |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation.md)  
[ISimulation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation_members.md)
