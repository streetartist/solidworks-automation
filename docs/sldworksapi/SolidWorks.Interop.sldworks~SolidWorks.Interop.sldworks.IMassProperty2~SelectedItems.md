# SelectedItems Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~SelectedItems`

Gets or sets the list of bodies/components for which to calculate mass properties.
Gets or sets the list of bodies/components for which to calculate mass properties.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SelectedItems As System.Object
```

```

Dim instance As IMassProperty2
Dim value As System.Object
 
instance.SelectedItems = value
 
value = instance.SelectedItems
```

```

System.object SelectedItems {get; set;}
```

```

property System.Object^ SelectedItems {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) for the part or [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) for the assembly

Remarks

Pre-selected bodies/components are included in the returned array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md)  
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.md)  
[IMassProperty2::IncludeHiddenBodiesOrComponents Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~IncludeHiddenBodiesOrComponents.md)
