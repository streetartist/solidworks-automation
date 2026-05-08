# DoNotChangeItemNumber Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData~DoNotChangeItemNumber`

Gets and sets whether to change BOM item numbers after sorting.
Gets and sets whether to change BOM item numbers after sorting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DoNotChangeItemNumber As System.Boolean
```

```

Dim instance As IBomTableSortData
Dim value As System.Boolean
 
instance.DoNotChangeItemNumber = value
 
value = instance.DoNotChangeItemNumber
```

```

System.bool DoNotChangeItemNumber {get; set;}
```

```

property System.bool DoNotChangeItemNumber {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to preserve BOM item numbers, false to re-number them

Example

See the [IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableSortData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md)  
[IBomTableSortData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData_members.md)
