# GetExtensionLineAsCenterline Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetExtensionLineAsCenterline`

Gets whether the specified extension line is a centerline.
Gets whether the specified extension line is a centerline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExtensionLineAsCenterline( _
   ByVal ExtIndex As System.Short, _
   ByRef Centerline As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim ExtIndex As System.Short
Dim Centerline As System.Boolean
Dim value As System.Boolean
 
value = instance.GetExtensionLineAsCenterline(ExtIndex, Centerline)
```

```

System.bool GetExtensionLineAsCenterline( 
   System.short ExtIndex,
   out System.bool Centerline
)
```

```

System.bool GetExtensionLineAsCenterline( 
   System.short ExtIndex,
   [Out] System.bool Centerline
) 
```

#### Parameters

*ExtIndex*
:   Index of extension line

*Centerline*
:   True if the extension line is a centerline, false if not

#### Return Value

True if successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
