# GetProfileItems Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetProfileItems`

Gets the sketch segments that make up this detail circle profile.
Gets the sketch segments that make up this detail circle profile.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetProfileItems() As System.Object
```

```

Dim instance As IDetailCircle
Dim value As System.Object
 
value = instance.GetProfileItems()
```

```

System.object GetProfileItems()
```

```

System.Object^ GetProfileItems(); 
```

#### Return Value

Array of the [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) that make up this detail circle profile

Remarks

Do not modify the sketch segments returned by this method. This method only provides information about the profile geometry of the detail circle. To modify a detail circle, use [IDetailCircle::SetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetParameters.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::IGetProfileItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~IGetProfileItems.md)  
[IDetailCircle::GetProfileItemsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetProfileItemsCount.md)
