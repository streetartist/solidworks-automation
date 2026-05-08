# SetAllOverThisSide Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetAllOverThisSide`

Sets whether this Gtol uses an All Over This Side leader.
Sets whether this Gtol uses an All Over This Side leader.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetAllOverThisSide( _
   ByVal AllOverTS As System.Boolean _
) 
```

```

Dim instance As IGtol
Dim AllOverTS As System.Boolean
 
instance.SetAllOverThisSide(AllOverTS)
```

```

void SetAllOverThisSide( 
   System.bool AllOverTS
)
```

```

void SetAllOverThisSide( 
   System.bool AllOverTS
) 
```

#### Parameters

*AllOverTS*
:   True to use an All Over This Side leader, false to not

Remarks

This property is valid only for bent, perpendicular, and multi-jog leaders.

Use:

- [IGtol::IsAttached](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IsAttached.md) to determine whether this symbol is currently using a leader.
- [IGtol::HasExtraLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~HasExtraLeader.md) to determine whether this symbol is using a bent leader.
- [IGtol::GetLeaderSide](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderSide.md) to determine where the leader is attached to the symbol.
- [IGtol::SetLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetLeader.md) to set the characteristics of the leader on this symbol.

Example

'VBA Preconditions:

'Open a drawing.

```

Dim swApp As SldWorks  
Dim Part As ModelDoc2  
Dim myGtol As Gtol  
Dim myAnno As Annotation  
Dim boolstatus As Boolean  
Dim longstatus As Long, longwarnings As Long  
Option Explicit  
Sub main()
```

```

    Set swApp = Application.SldWorks  
    Set Part = swApp.ActiveDoc  
      
    Set myGtol = Part.InsertGtol()  
    If Not myGtol Is Nothing Then  
       myGtol.SetFrameSymbols2 1, "<IGTOL-SPROF>", False, "", False, "", "", "", ""  
       myGtol.SetFrameValues 1, ".031265", "", "", "", ""  
       myGtol.SetFrameSymbols2 2, "", False, "", False, "", "", "", ""  
       myGtol.SetFrameValues 2, "", "", "", "", ""  
       myGtol.SetPTZHeight "", False  
       myGtol.SetCompositeFrame False  
       myGtol.SetText 4, ""  
       myGtol.SetBetweenTwoPoints False, "", ""  
       myGtol.SetAllOverThisSide True  
       Set myAnno = myGtol.GetAnnotation()  
       If Not myAnno Is Nothing Then  
          boolstatus = myAnno.SetPosition(0.801796955941255, 0.800162656875834, 0)  
          longstatus = myAnno.SetLeader3(swLeaderStyle_e.swBENT, 0, True, False, False, False)  
       End If  
    End If  
    Part.WindowRedraw
```

```

End Sub 
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetAllOverThisSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAllOverThisSide.md)  
[IGtol::SetAllAroundThisSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetAllAroundThisSide.md)
