# Callout Property (ISelectData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Callout`

Gets or sets the callout to attach to the selected object.
Gets or sets the callout to attach to the selected object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Callout As Callout
```

```

Dim instance As ISelectData
Dim value As Callout
 
instance.Callout = value
 
value = instance.Callout
```

```

Callout Callout {get; set;}
```

```

property Callout^ Callout {
   Callout^ get();
   void set (    Callout^ value);
}
```

#### Property Value

[Callout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md) to which to attach the selected object

Remarks

This property is not used by [IModelDocExtension::MultiSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect.md) or [IModelDocExtension::IMultiSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IMultiSelect.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md)  
[ISelectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData_members.md)
