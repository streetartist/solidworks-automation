# SelectiveSectioningList Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSectioningList`

Gets or sets the bodies in the multibody part or the components in the assembly for selective sectioning in this section view.
Gets or sets the bodies in the multibody part or the components in the assembly for selective sectioning in this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SelectiveSectioningList As System.Object
```

```

Dim instance As ISectionViewData
Dim value As System.Object
 
instance.SelectiveSectioningList = value
 
value = instance.SelectiveSectioningList
```

```

System.object SelectiveSectioningList {get; set;}
```

```

property System.Object^ SelectiveSectioningList {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) in the multibody part or an array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) in the assembly to selectively section (see **Remarks**)

Remarks

To select each body in a multibody part or each component in an assembly for selective sectioning, specify a Mark of 8 for [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md). Select the section planes after selecting the bodies or components.

Call [ISectionViewData::ExcludeSelectedItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ExcludeSelectedItems.md) to exclude or include the specified bodies in the multibody part or the specified components in the assembly in selective sectioning.

ISectionViewData::SelectiveSectioningList is only available if [ISectionViewData::SelectiveSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSection.md) is true.

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
[ISectionViewData::FirstPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~FirstPlane.md)  
[ISectionViewData::SecondPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondPlane.md)  
[ISectionViewData::ThirdPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdPlane.md)
