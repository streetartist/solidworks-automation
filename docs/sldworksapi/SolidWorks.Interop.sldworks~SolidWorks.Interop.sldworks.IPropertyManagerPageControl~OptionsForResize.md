# OptionsForResize Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~OptionsForResize`

Gets or sets how to override the SOLIDWORKS default behavior when changing the width of a PropertyManager page.
Gets or sets how to override the SOLIDWORKS default behavior when changing the width of a PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OptionsForResize As System.Integer
```

```

Dim instance As IPropertyManagerPageControl
Dim value As System.Integer
 
instance.OptionsForResize = value
 
value = instance.OptionsForResize
```

```

System.int OptionsForResize {get; set;}
```

```

property System.int OptionsForResize {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Resize the PropertyManager page as defined in [swPropMgrPageControlOnResizeOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropMgrPageControlOnResizeOptions_e.html) (see **Remarks**)

Remarks

|  |  |
| --- | --- |
| **If...** | **Then...** |
| swControlOptionsOnResize\_LockLeft specified | the control is locked in place relative to the left edge of the PropertyManager page. When the page width is changed, the control stays in place and its width does not change. |
| swControlOptionsOnResize\_LockRight specified | the control is locked in place relative to the right edge of the PropertyManager page. When the page width is changed, the control shifts to the right, but its width does not change. |
| swControlOptionsOnResize\_LockLeft and swControlOptionsOnResize\_LockRight specified | the left edge of the control stays in place relative to the left edge and the right edge of the control stays in place relative to the right edge of the PropertyManager page, giving the effect that the control grows and shrinks with the PropertyManager page. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.md)  
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.md)
