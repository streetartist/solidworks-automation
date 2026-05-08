# SetLineInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetLineInfo`

Sets the location (both position and arrow heads) of the section line.
Sets the location (both position and arrow heads) of the section line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLineInfo( _
   ByVal VLineInfo As System.Object _
) As System.Boolean
```

```

Dim instance As IDrSection
Dim VLineInfo As System.Object
Dim value As System.Boolean
 
value = instance.SetLineInfo(VLineInfo)
```

```

System.bool SetLineInfo( 
   System.object VLineInfo
)
```

```

System.bool SetLineInfo( 
   System.Object^ VLineInfo
) 
```

#### Parameters

*VLineInfo*
:   Array  (see **Remarks**)

Remarks

The VLineInfo argument is an array consisting of several coordinate pairs and is of the same format as the array returned by [IDrSection::GetLineInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetLineInfo.md). The number of coordinate pairs is determined by the number of line segments in the section line. Each coordinate pair consists of 6 doubles, the x,y,z coordinate of  
each end point of the segment.

The formatted array should include the start point and end point of each line segment, including the z position even though the z position is irrelevant.

Any section line containing more than one segment contains at least one set of duplicate points. These points represent the end point of one line segment and the coincident start point of another line segment. If you change either set of points, then you must change the other set of points at the same time. These points must always be  
coincident when calling this method.

To update the section view, call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) after calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::IGetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetLineInfo.md)  
[IDrSection::IGetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetLineInfo.md)
