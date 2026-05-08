# SelectiveSection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSection`

Gets or sets whether selective sectioning is enabled in this section view.
Gets or sets whether selective sectioning is enabled in this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SelectiveSection As System.Boolean
```

```

Dim instance As ISectionViewData
Dim value As System.Boolean
 
instance.SelectiveSection = value
 
value = instance.SelectiveSection
```

```

System.bool SelectiveSection {get; set;}
```

```

property System.bool SelectiveSection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if selective sectioning is enabled, false if not (see **Remarks**)

Remarks

| If this property is... | Then... |
| --- | --- |
| True | You can specify which bodies in the multibody part or which components in the assembly to selectively section. Call:   - [ISectionViewData::SelectiveSectioningList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSectioningList.md) to specify the bodies or components to selectively section.  - [ISectionViewData::ExcludeSelectedItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ExcludeSelectedItems.md) to specify the bodies or components to exclude or include in selective sectioning. |
| False | All bodies in the multibody part and all components in the assembly are sectioned. |

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
[ISectionViewData::TransparentSection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparentSection.md)
