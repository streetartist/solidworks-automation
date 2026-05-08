# Size Property (IAdvancedHoleElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~Size`

Gets or sets the size of this Advanced Hole element.
Gets or sets the size of this Advanced Hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Size As System.String
```

```

Dim instance As IAdvancedHoleElementData
Dim value As System.String
 
instance.Size = value
 
value = instance.Size
```

```

System.string Size {get; set;}
```

```

property System.String^ Size {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Size specific to the type of hole element

Remarks

The size must be appropriate for the [IAdvancedHoleElementData::FastenerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~FastenerType.md).

Valid sizes are listed in the Element Specification section of the Advanced Hole PropertyManager. Select a type from the Type dropdown and inspect the Size dropdown for valid sizes.

Example

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md)  
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.md)
