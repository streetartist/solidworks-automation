# GetProfileItemsCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetProfileItemsCount`

Gets the number of sketch segments that make up this detail circle profile.
Gets the number of sketch segments that make up this detail circle profile.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetProfileItemsCount() As System.Integer
```

```

Dim instance As IDetailCircle
Dim value As System.Integer
 
value = instance.GetProfileItemsCount()
```

```

System.int GetProfileItemsCount()
```

```

System.int GetProfileItemsCount(); 
```

#### Return Value

Number of sketch segments that make up this detail circle profile

Remarks

Call this method before calling [IDetailCircle::IGetProfileItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~IGetProfileItems.md) to determine the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::GetProfileItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetProfileItems.md)
