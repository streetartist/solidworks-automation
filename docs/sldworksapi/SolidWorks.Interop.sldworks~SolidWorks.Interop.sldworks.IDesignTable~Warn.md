# Warn Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~Warn`

Gets or sets whether to display a warning when invalid information is encountered in the design table when updating the design table.
Gets or sets whether to display a warning when invalid information is encountered in the design table when updating the design table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Warn As System.Boolean
```

```

Dim instance As IDesignTable
Dim value As System.Boolean
 
instance.Warn = value
 
value = instance.Warn
```

```

System.bool Warn {get; set;}
```

```

property System.bool Warn {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display a warning when invalid information is encountered in the design table when updating the design table, false to not

Remarks

If information is entered to the left of the parameters row or below the configuration name column, then the SOLIDWORKS software warns of an invalid value and stops processing the design table without completing the remaining rows and columns. If this happens, some configurations do not update properly.

You must call:

- [IDesignTable::EditFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditFeature.md) before setting this property.
- [IDesignTable::UpdateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.md) after setting this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)  
[IDesignTable::UpdateTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateTable.md)
