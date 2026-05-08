# AddTab Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddTab`

Adds a tab to a PropertyManager page.
Adds a tab to a PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddTab( _
   ByVal ID As System.Integer, _
   ByVal Caption As System.String, _
   ByVal Bitmap As System.String, _
   ByVal Options As System.Integer _
) As PropertyManagerPageTab
```

```

Dim instance As IPropertyManagerPage2
Dim ID As System.Integer
Dim Caption As System.String
Dim Bitmap As System.String
Dim Options As System.Integer
Dim value As PropertyManagerPageTab
 
value = instance.AddTab(ID, Caption, Bitmap, Options)
```

```

PropertyManagerPageTab AddTab( 
   System.int ID,
   System.string Caption,
   System.string Bitmap,
   System.int Options
)
```

```

PropertyManagerPageTab^ AddTab( 
   System.int ID,
   System.String^ Caption,
   System.String^ Bitmap,
   System.int Options
) 
```

#### Parameters

*ID*
:   Identifier defined by the add-in for this tab

*Caption*
:   Text for tab

*Bitmap*
:   Bitmap for tab

*Options*
:   Not used; specify 0

#### Return Value

Newly created [PropertyManager page tab](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab.md)

Remarks

The ID argument provides an add-in with a way of identifying which tab is being handled when one of the callbacks is called; for example, when [IPropertyManagerPage2Handler8::OnTabClicked](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnTabClicked.md) is called. The IDis passed as an argument, identifying the tab clicked.

The Bitmap argument allows you to place a bitmap before the text on the tab. The argument is the full path and filename to a bitmap on disk. The bitmap should be 16 x 18 (width x height) pixels. It can be either 16 or 256 colors. Any portions of the bitmap that are RGB(255,255,255) will be transparent, letting the tab background show through. If this argument is an empty string or not the name of a valid bitmap file, no bitmap is placed on the tab.

 

Use this method to add tabs to your PropertyManager page before the page is displayed. It cannot be used if the page is already displayed.

Use [IPropertyManagerPageTab::Caption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~Caption.md) to add a caption to the tab.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)
