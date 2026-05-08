# NextReference Method (IRibFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~NextReference`

Cycles through the possible sketch entities that can be used to define the draft, if it is used, for ribs with multiple contours.
Cycles through the possible sketch entities that can be used to define the draft, if it is used, for ribs with multiple contours.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function NextReference() As System.Integer
```

```

Dim instance As IRibFeatureData2
Dim value As System.Integer
 
value = instance.NextReference()
```

```

System.int NextReference()
```

```

System.int NextReference(); 
```

#### Return Value

Index of the entity that is used

Remarks

This method cycles through the entities. It starts at the beginning again once the last entity is reached.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md)  
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.md)
