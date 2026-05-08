# ExcludeSelectedItems Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ExcludeSelectedItems`

Gets or sets whether to exclude or include the specific bodies in the multibody part or specific components in the assembly in selective sectioning in this section view.
Gets or sets whether to exclude or include the specific bodies in the multibody part or specific components in the assembly in selective sectioning in this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ExcludeSelectedItems As System.Boolean
```

```

Dim instance As ISectionViewData
Dim value As System.Boolean
 
instance.ExcludeSelectedItems = value
 
value = instance.ExcludeSelectedItems
```

```

System.bool ExcludeSelectedItems {get; set;}
```

```

property System.bool ExcludeSelectedItems {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to exclude specific bodies in the multibody part or specific components in the assembly in selective sectioning, false to include only the specific bodies in the part or the specific components in the assembly in selective sectioning (see **Remarks**)

Remarks

Before calling this property, call [ISectionViewData::SelectiveSectioningList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSectioningList.md) to specify the bodies in the multibody part or the components in the assembly to exclude or include in selective sectioning.

ISectionViewData::ExcludeSelectedItems is only available if [ISectionViewData::SelectiveSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSection.md) is true.

Example

[Selectively and Transparently Section a Section View (C#)](Selectively_and_Transparently_Section_a_Section_View_Example_CSharp.htm)  
[Selectively and Transparently Section a Section View (VB.NET)](Selectively_and_Transparently_Section_a_Section_View_Example_VBNET.htm)  
[Selectively and Transparently Section a Section View (VBA)](Selectively_and_Transparently_Section_a_Section_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md)  
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.md)
