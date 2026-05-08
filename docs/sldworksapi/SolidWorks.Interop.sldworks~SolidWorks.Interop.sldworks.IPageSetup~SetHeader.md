# SetHeader Method (IPageSetup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetHeader`

Sets the entire page header.
Sets the entire page header.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetHeader( _
   ByVal Left As System.String, _
   ByVal Center As System.String, _
   ByVal Right As System.String _
) As System.Boolean
```

```

Dim instance As IPageSetup
Dim Left As System.String
Dim Center As System.String
Dim Right As System.String
Dim value As System.Boolean
 
value = instance.SetHeader(Left, Center, Right)
```

```

System.bool SetHeader( 
   System.string Left,
   System.string Center,
   System.string Right
)
```

```

System.bool SetHeader( 
   System.String^ Left,
   System.String^ Center,
   System.String^ Right
) 
```

#### Parameters

*Left*
:   Left-header text

*Center*
:   Center-header text

*Right*
:   Right-header text

#### Return Value

True if the header is successfully changed, false if not

Remarks

This method is equivalent to setting [IPageSetup:LeftHeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftHeader.md), [IPageSetup::CenterHeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterHeader.md), and [IPageSetup::RightHeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightHeader.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md)  
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.md)  
[IPageSetup::GetHeaderFooterString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetHeaderFooterString.md)  
[IPageSetup::SetFooter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetFooter.md)  
[IPageSetup::CenterFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterFooter.md)  
[IPageSetup::FooterTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~FooterTextFormat.md)  
[IPageSetup::HeaderTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~HeaderTextFormat.md)  
[IPageSetup::LeftFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftFooter.md)  
[IPageSetup::RightFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightFooter.md)
