# SetFullOutline Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetFullOutline`

Sets whether the complete detail circle or detail profile is shown in the detail view, or if just the part of the circle or profile that intersects the view geometry is shown.
Sets whether the complete detail circle or detail profile is shown in the detail view, or if just the part of the circle or profile that intersects the view geometry is shown.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFullOutline( _
   ByVal FullOutline As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDetailCircle
Dim FullOutline As System.Boolean
Dim value As System.Boolean
 
value = instance.SetFullOutline(FullOutline)
```

```

System.bool SetFullOutline( 
   System.bool FullOutline
)
```

```

System.bool SetFullOutline( 
   System.bool FullOutline
) 
```

#### Parameters

*FullOutline*
:   True if the full circle or profile outline is shown in the detail view, false if only the portion of the circle or profile that intersects the view geometry is shown

#### Return Value

True if setting the full outline flag is successful, false if not

Remarks

This method:

- is only available when [IDetailCircle::NoOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~NoOutline.md) is false.
- automatically loads the model for the detail view if necessary, without prompting the user.

If the style of the detail circle (see [IDetailCircle::GetStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetStyle.md)) is swDetViewCONNECTED, then this method cannot disable the full outline because the full outline of the circle or profile must be shown.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::HasFullOutline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~HasFullOutline.md)
