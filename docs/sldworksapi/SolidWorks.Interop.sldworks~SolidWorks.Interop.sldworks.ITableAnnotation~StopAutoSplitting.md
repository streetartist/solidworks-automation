# StopAutoSplitting Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~StopAutoSplitting`

Stops the automatic horizontal splitting of this table.
Stops the automatic horizontal splitting of this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property StopAutoSplitting As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim value As System.Boolean
 
instance.StopAutoSplitting = value
 
value = instance.StopAutoSplitting
```

```

System.bool StopAutoSplitting {get; set;}
```

```

property System.bool StopAutoSplitting {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to stop the automatic horizontal splitting of this table, false to not

Remarks

This property works with [ITableAnnotation::HorizontalAutoSplit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~HorizontalAutoSplit.md) to control the automatic horizontal splitting of:

- [Hole tables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation.md)
- [Bill of Materials tables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)
- [General tables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableAnnotation.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::Split Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Split.md)  
[ITableAnnotation::GetSplitInformation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetSplitInformation.md)
