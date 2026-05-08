# SetPrecision Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetPrecision`

Obsolete. Superseded by IDisplayDimension::SetPrecision2.
Obsolete. Superseded by [IDisplayDimension::SetPrecision2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetPrecision2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPrecision( _
   ByVal UseDoc As System.Boolean, _
   ByVal Primary As System.Integer, _
   ByVal Alternate As System.Integer, _
   ByVal PrimaryTol As System.Integer, _
   ByVal AlternateTol As System.Integer _
) As System.Integer
```

```

Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim Primary As System.Integer
Dim Alternate As System.Integer
Dim PrimaryTol As System.Integer
Dim AlternateTol As System.Integer
Dim value As System.Integer
 
value = instance.SetPrecision(UseDoc, Primary, Alternate, PrimaryTol, AlternateTol)
```

```

System.int SetPrecision( 
   System.bool UseDoc,
   System.int Primary,
   System.int Alternate,
   System.int PrimaryTol,
   System.int AlternateTol
)
```

```

System.int SetPrecision( 
   System.bool UseDoc,
   System.int Primary,
   System.int Alternate,
   System.int PrimaryTol,
   System.int AlternateTol
) 
```

#### Parameters

*UseDoc*

*Primary*

*Alternate*

*PrimaryTol*

*AlternateTol*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
